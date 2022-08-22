from django.apps import AppConfig

class EBHealthCheckConfig(AppConfig):
    name = 'ebhealthcheck'

    def ready(self):
        """
        Fix for the EB health check host header:

        https://aalvarez.me/posts/setting-up-elastic-beanstalk-health-checks-with-a-django-application/
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
        """

        from django.conf import settings
        import requests

        def get_ec2_instance_ip():
            metadata_url = "http://169.254.169.254/latest"
            n = 0
            while n < 10:
                try:
                    token = requests.put(metadata_url + "/api/token", timeout=0.1, headers={
                        "X-aws-ec2-metadata-token-ttl-seconds": "60",
                    }).text
                    ip = requests.get(metadata_url + "/meta-data/local-ipv4", timeout=0.1, headers={
                        "X-aws-ec2-metadata-token": token,
                    }).text
                except (requests.exceptions.ConnectionError, requests.exceptions.InvalidHeader):
                    n += 1
                    continue
                else:
                    return ip
            return None

        public_ip = get_ec2_instance_ip()
        if public_ip:
            settings.ALLOWED_HOSTS.append(public_ip)
