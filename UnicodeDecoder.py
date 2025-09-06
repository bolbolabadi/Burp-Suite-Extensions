# -*- coding: utf-8 -*-
from burp import IBurpExtender, IMessageEditorTabFactory, IMessageEditorTab
import codecs

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Unicode Decoder")
        callbacks.registerMessageEditorTabFactory(self)

    def createNewInstance(self, controller, editable):
        return UnicodeDecoderTab(self, controller, editable)


class UnicodeDecoderTab(IMessageEditorTab):

    def __init__(self, extender, controller, editable):
        self._extender = extender
        self._controller = controller
        self._editable = editable
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(False)
        self._currentMessage = None

    def getTabCaption(self):
        return "Unicode Decoded"

    def getUiComponent(self):
        return self._txtInput.getComponent()

    def isEnabled(self, content, isRequest):
        return True  # Always enable

    def setMessage(self, content, isRequest):
        if content is None:
            self._txtInput.setText(None)
            self._currentMessage = None
            return

        try:
            message_str = content.tostring()
            # Decode \uXXXX sequences into readable Unicode
            decoded = message_str.encode("utf-8").decode("unicode_escape")
        except Exception:
            decoded = message_str

        self._txtInput.setText(decoded.encode("utf-8"))
        self._currentMessage = content

    def getMessage(self):
        return self._currentMessage

    def isModified(self):
        return False

    def getSelectedData(self):
        return self._txtInput.getSelectedText()
