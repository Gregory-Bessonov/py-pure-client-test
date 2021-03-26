from pypureclient.flashblade import CertificatePost

# create a new external certificate named "ad-cert-1"
cert_name = 'ad-cert-1'
cert_text = '-----BEGIN CERTIFICATE-----\nMIIESzCCAzOgAwIBAgIJAIJMKJXXDn/JMA0GCSqGSIb3DQEBBQUAMHYxCzAJBgNV\nBAYTAlVTMQ0wCwYDVQQIEwR0ZXN0MQ4wDAYDVQQHEwV0ZXN0IDENMAsGA1UEChME\ndGVzdDENMAsGA1UECxMEdGVzdDEVMBMGA1UEAxMMUHVyZSBTdG9yYWdlMRMwEQYJ\nKoZIhvcNAQkBFgR0ZXN0MB4XDTE3MTEwNjIyMzYyMFoXDTE4MTEwNjIyMzYyMFow\ndjELMAkGA1UEBhMCVVMxDTALBgNVBAgTBHRlc3QxDjAMBgNVBAcTBXRlc3QgMQ0w\nCwYDVQQKEwR0ZXN0MQ0wCwYDVQQLEwR0ZXN0MRUwEwYDVQQDEwxQdXJlIFN0b3Jh\nZ2UxEzARBgkqhkiG9w0BCQEWBHRlc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw\nggEKAoIBAQDcaGpPXJC1EC515wMEKyXEFuKFEDn4y1V5YmaLt+hXz8cfuA+gS3eD\nltP8PJah+7WrPouUQtfamHsuQtnFFLcVcdl83rIFX0m58zUiWbOUHI5wWnBYsqof\n52k/m40HM5XTATn5xpFsTSxm7vmlsKfGlQS7yI11HbD0OOz9CqT+iMFhTn/Wfyg2\nYOtmYIfCz0kt6wIFHlI9oPERwJ0JiMnPhsg0gerJwYl1j1vDhBiK32OVc4iIdOO4\nPVwpP1YbINr8LJ5qX2DOzBHDnaYrtJk9YEsSAwoqJ2/d29xA9JOeJwahl/M6aO48\nAbXbSlxVwOz0lEs85dseLp9dyTQb/uzjAgMBAAGjgdswgdgwHQYDVR0OBBYEFJJM\nML8khiOYzpaJP8sJCn0JSpx9MIGoBgNVHSMEgaAwgZ2AFJJMML8khiOYzpaJP8sJ\nCn0JSpx9oXqkeDB2MQswCQYDVQQGEwJVUzENMAsGA1UECBMEdGVzdDEOMAwGA1UE\nBxMFdGVzdCAxDTALBgNVBAoTBHRlc3QxDTALBgNVBAsTBHRlc3QxFTATBgNVBAMT\nDFB1cmUgU3RvcmFnZTETMBEGCSqGSIb3DQEJARYEdGVzdIIJAIJMKJXXDn/JMAwG\nA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBAKjQ/SFPra2YmtNynNukuHOl\nCryjsXjBkeiyyfg3Bt9+M+9F6Y4Sh3/SSJCb6LQaqTQkeJJeb1fOHNaFjAxkjvaI\n2tnlCwhpQuoSXNgQEMdidMi9+S8hBonlXYePYZUQbvAu1VAZrU6f0k2OEDcAPLvA\nhZLvrmZeug+VZp3JfVOdU+QnzUx2atBBfN5lMFFNdqOzZ5Yz/Ooi9CVA73szIevi\nE728OLimWQ91u1s16isjusK3+zoqirFC7PN6K63sp0gPAldgCQD2bywmwgaYDnzP\n+9ZWNy6ebn927Qh22YUPWhj+kiITkhxcVYPMx4QtRjJhs5pQVBqHOIDnJQJc7qY=\n-----END CERTIFICATE-----'
cert_type = 'external'
create_body = CertificatePost(certificate=cert_text, certificate_type=cert_type)
res = client.post_certificates(names=[cert_name], certificate=create_body)
print(res)
if type(res) == pypureclient.responses.ValidResponse:
    print(list(res.items))