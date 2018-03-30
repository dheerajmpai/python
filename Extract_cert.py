def getpeercert(self):
                import ssl
                cert = None
                if self.sock:
                        cert =  self.sock.getpeercert()
                else:
                        cert = ssl.get_server_certificate((self.host,self.port),
                                ssl_version=ssl.PROTOCOL_SSLv23 )
                        lf = (len(ssl.PEM_FOOTER)+1)
                        if cert[0-lf] != '\n':
                                cert = cert[:0-lf]+'\n'+cert[0-lf:]
                        log.debug("len-footer: %s cert: %r", lf, cert[0-lf])
                
                return cert
           
