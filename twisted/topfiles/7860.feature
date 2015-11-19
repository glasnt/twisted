twisted.internet.ssl.CertificateOptions and twisted.internet.ssl.optionsForClientTLS now take a acceptableProtocols parameter that enables negotiation of the next protocol to speak after the TLS handshake has completed. This field advertises protocols over both NPN and ALPN. Also added new INegotiated interface for TLS interfaces that support protocol negotiation. This interface adds a negotiatedProtocol property that reports what protocol, if any, was negotiated in the TLS handshake.