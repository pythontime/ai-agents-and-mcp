with Diagram("DNS Reliability Demo - Multi-Region Failover Architecture", show=False, direction="TB"):
    # Route 53 for DNS failover
    dns = Route53("Route 53\nFailover DNS")
    
    # Shared IAM resources
    with Cluster("Shared IAM Resources"):
        iam_role = IAMRole("EC2-SSM-Role")
        iam_policy = IAMPermissions("SSM Policy\nAttachment")
        iam_role >> iam_policy
    
    # Primary Region - us-east-2
    with Cluster("Primary Region (us-east-2)"):
        with Cluster("VPC (Default)"):
            primary_subnet = PublicSubnet("Subnet")
            primary_sg = Nacl("Security Group\n(HTTP/HTTPS)")
            primary_ec2 = EC2Instance("Primary Web Server\nt4g.micro\nApache + Health Check")
            
            primary_subnet >> primary_sg >> primary_ec2
    
    # Secondary Region - us-west-2  
    with Cluster("Secondary Region (us-west-2)"):
        with Cluster("VPC (Default)"):
            secondary_subnet = PublicSubnet("Subnet")
            secondary_sg = Nacl("Security Group\n(HTTP/HTTPS)")
            secondary_ec2 = EC2Instance("Secondary Web Server\nt4g.micro\nApache + Health Check")
            
            secondary_subnet >> secondary_sg >> secondary_ec2
    
    # Connections
    dns >> Edge(label="Primary\nHealth Check", color="green") >> primary_ec2
    dns >> Edge(label="Secondary\nFailover", color="orange", style="dashed") >> secondary_ec2
    
    # IAM connections
    iam_role >> Edge(label="Instance Profile", style="dotted") >> primary_ec2
    iam_role >> Edge(label="Instance Profile", style="dotted") >> secondary_ec2