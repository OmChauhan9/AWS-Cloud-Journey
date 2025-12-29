[Private subnet.drawio](https://github.com/user-attachments/files/24364207/Private.subnet.drawio)# Creating a Private Subnet

## 🎯 Project Goal
To implement a "Zero Trust" network foundation by creating a **Private Subnet** that is completely isolated from the public internet. The goal was to configure routing and firewalls (NACLs) to strictly control traffic flow.

## ⚙️ Architecture Stats
* **VPC CIDR:** `10.0.0.0/16`
* **Private Subnet CIDR:** `10.0.1.0/24`
* **Availability Zone:** `us-east-1a`
* **Internet Access:** **None** (No Internet Gateway attached)<br>

  [Uploading<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15" version="29.2.9">
  <diagram name="Page-1" id="VuVDFcHFMxcprFpfoxO2">
    <mxGraphModel dx="1296" dy="756" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="qKhLzYYokemrFDp-wy6_-62" parent="1" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud;strokeColor=#232F3E;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#232F3E;dashed=0;" value="AWS Cloud" vertex="1">
          <mxGeometry height="520" width="720" x="160" y="120" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-63" parent="qKhLzYYokemrFDp-wy6_-62" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;" value="VPC" vertex="1">
          <mxGeometry height="440" width="600" x="80" y="40" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-64" parent="qKhLzYYokemrFDp-wy6_-63" style="fillColor=none;strokeColor=#147EBA;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#147EBA;whiteSpace=wrap;html=1;" value="Availability Zone" vertex="1">
          <mxGeometry height="360" width="520" x="40" y="40" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-65" parent="qKhLzYYokemrFDp-wy6_-63" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#7AA116;fillColor=#F2F6E8;verticalAlign=top;align=left;spacingLeft=30;fontColor=#248814;dashed=0;" value="Public subnet" vertex="1">
          <mxGeometry height="133" width="130" x="390" y="200" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-83" parent="qKhLzYYokemrFDp-wy6_-65" style="fillColor=none;strokeColor=#DD3522;verticalAlign=top;fontStyle=0;fontColor=#DD3522;whiteSpace=wrap;html=1;" value="Security group" vertex="1">
          <mxGeometry height="90" width="110" x="10" y="30" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-86" parent="qKhLzYYokemrFDp-wy6_-65" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.ec2;fillColor=#F58534;gradientColor=none;" value="" vertex="1">
          <mxGeometry height="40" width="60" x="35" y="60" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-66" parent="qKhLzYYokemrFDp-wy6_-63" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;" value="Private subnet" vertex="1">
          <mxGeometry height="130" width="130" x="390" y="60" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-72" parent="qKhLzYYokemrFDp-wy6_-63" style="fillColor=#EFF0F3;strokeColor=none;dashed=0;verticalAlign=top;fontStyle=0;fontColor=#232F3D;whiteSpace=wrap;html=1;" value="Route Tables" vertex="1">
          <mxGeometry height="270" width="130" x="120" y="60" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-77" parent="qKhLzYYokemrFDp-wy6_-63" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.route_table;fillColor=#F58536;gradientColor=none;" value="" vertex="1">
          <mxGeometry height="50" width="52" x="159" y="230" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-78" parent="qKhLzYYokemrFDp-wy6_-63" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.route_table;" value="" vertex="1">
          <mxGeometry height="50" width="51.32" x="159" y="90" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-81" parent="qKhLzYYokemrFDp-wy6_-63" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor=#FF6A00;strokeColor=none;shape=mxgraph.alibaba_cloud.network_acl_access_control_list;" value="" vertex="1">
          <mxGeometry height="42.599999999999994" width="47.400000000000006" x="290" y="98" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-82" parent="qKhLzYYokemrFDp-wy6_-63" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor=#FF6A00;strokeColor=none;shape=mxgraph.alibaba_cloud.network_acl_access_control_list;" value="" vertex="1">
          <mxGeometry height="46.3" width="51.52" x="290" y="233.7" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-84" parent="qKhLzYYokemrFDp-wy6_-63" style="strokeWidth=1;shadow=0;dashed=0;align=center;html=1;shape=mxgraph.mockup.text.textBox;fontColor=#666666;align=left;fontSize=17;spacingLeft=4;spacingTop=-3;whiteSpace=wrap;strokeColor=#666666;mainText=" value="&lt;h6&gt;&lt;font face=&quot;Times New Roman&quot; style=&quot;font-weight: normal;&quot;&gt;&lt;span style=&quot;font-size: 12px; line-height: 90%;&quot;&gt;Private Route&lt;/span&gt;&lt;font style=&quot;font-size: 9px; line-height: 90%;&quot;&gt; &lt;/font&gt;&lt;span style=&quot;font-size: 12px; line-height: 100%;&quot;&gt;Table&lt;/span&gt;&lt;/font&gt;&lt;/h6&gt;" vertex="1">
          <mxGeometry height="20" width="110" x="130" y="150" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-85" parent="qKhLzYYokemrFDp-wy6_-63" style="strokeWidth=1;shadow=0;dashed=0;align=center;html=1;shape=mxgraph.mockup.text.textBox;fontColor=#666666;align=left;fontSize=17;spacingLeft=4;spacingTop=-3;whiteSpace=wrap;strokeColor=#666666;mainText=" value="&lt;h6&gt;&lt;font face=&quot;Times New Roman&quot; style=&quot;font-weight: normal;&quot;&gt;&lt;span style=&quot;font-size: 12px; line-height: 90%;&quot;&gt;Public Route&lt;/span&gt;&lt;font style=&quot;font-size: 9px; line-height: 90%;&quot;&gt; &lt;/font&gt;&lt;span style=&quot;font-size: 12px; line-height: 100%;&quot;&gt;Table&lt;/span&gt;&lt;/font&gt;&lt;/h6&gt;" vertex="1">
          <mxGeometry height="20" width="110" x="129.65999999999997" y="290" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-87" parent="qKhLzYYokemrFDp-wy6_-63" style="strokeWidth=1;shadow=0;dashed=0;align=center;html=1;shape=mxgraph.mockup.text.textBox;fontColor=#666666;align=left;fontSize=17;spacingLeft=4;spacingTop=-3;whiteSpace=wrap;strokeColor=#666666;mainText=" value="&lt;h6 style=&quot;&quot;&gt;&lt;span style=&quot;line-height: 100%; font-weight: normal;&quot;&gt;&lt;font style=&quot;font-size: 11px;&quot;&gt;Private Network ACL&lt;/font&gt;&lt;/span&gt;&lt;/h6&gt;" vertex="1">
          <mxGeometry height="20" width="110" x="260.76" y="150" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-88" parent="qKhLzYYokemrFDp-wy6_-63" style="strokeWidth=1;shadow=0;dashed=0;align=center;html=1;shape=mxgraph.mockup.text.textBox;fontColor=#666666;align=left;fontSize=17;spacingLeft=4;spacingTop=-3;whiteSpace=wrap;strokeColor=#666666;mainText=" value="&lt;h6 style=&quot;&quot;&gt;&lt;span style=&quot;line-height: 100%; font-weight: normal;&quot;&gt;&lt;font style=&quot;font-size: 11px;&quot;&gt;Public Network ACL&lt;/font&gt;&lt;/span&gt;&lt;/h6&gt;" vertex="1">
          <mxGeometry height="20" width="110" x="270" y="290" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-79" parent="qKhLzYYokemrFDp-wy6_-62" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;strokeColor=#232F3E;fillColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.internet_gateway;" value="Internet&#xa;gateway" vertex="1">
          <mxGeometry height="60" width="60" x="10" y="270" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-80" parent="1" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;strokeColor=#232F3E;fillColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.user;" value="User" vertex="1">
          <mxGeometry height="50" width="50" x="40" y="390" as="geometry" />
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-90" edge="1" parent="1" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" target="qKhLzYYokemrFDp-wy6_-79" value="">
          <mxGeometry height="50" relative="1" width="50" as="geometry">
            <mxPoint x="100" y="420" as="sourcePoint" />
            <mxPoint x="150" y="370" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-92" edge="1" parent="1" source="qKhLzYYokemrFDp-wy6_-79" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" value="">
          <mxGeometry height="50" relative="1" width="50" as="geometry">
            <mxPoint x="320" y="420" as="sourcePoint" />
            <mxPoint x="390" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-94" edge="1" parent="1" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" value="">
          <mxGeometry height="50" relative="1" width="50" as="geometry">
            <mxPoint x="470" y="420" as="sourcePoint" />
            <mxPoint x="520" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-96" edge="1" parent="1" style="endArrow=classic;startArrow=classic;html=1;rounded=0;entryX=-0.03;entryY=0.337;entryDx=0;entryDy=0;entryPerimeter=0;" target="qKhLzYYokemrFDp-wy6_-83" value="">
          <mxGeometry height="50" relative="1" width="50" as="geometry">
            <mxPoint x="590" y="420" as="sourcePoint" />
            <mxPoint x="630" y="420" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-97" edge="1" parent="1" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" value="">
          <mxGeometry height="50" relative="1" width="50" as="geometry">
            <mxPoint x="470" y="280" as="sourcePoint" />
            <mxPoint x="530" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qKhLzYYokemrFDp-wy6_-98" edge="1" parent="1" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" value="">
          <mxGeometry height="50" relative="1" width="50" as="geometry">
            <mxPoint x="580" y="280" as="sourcePoint" />
            <mxPoint x="630" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
 Private subnet.drawio…]()


## 🛠️ Implementation Steps

### 1. The "Hidden" Subnet
I created a subnet specifically designed for sensitive workloads (like Databases).
* **Configuration:** Unlike standard subnets, I disabled "Auto-assign Public IP".
* **Result:** Instances launched here have no public addressable identity.

### 2. Custom Route Table (The Logic)
The defining feature of a private subnet is its routing.
* I created a custom Route Table: `aws-task5-private-rt`
* **The Critical Step:** I explicitly **did not** add a route to the Internet Gateway (`0.0.0.0/0`).
* **Traffic Flow:** The route table only allows `10.0.0.0/16 -> local`, meaning resources can talk to the VPC, but the internet cannot see them.

### 3. Network ACLs (The Firewall)
To implement **Defense in Depth**, I replaced the default "Allow All" Network ACL with a custom one.
* **Resource:** `aws-task5-private-nacl`
* **Rule Set:** Configured with a default **DENY** posture to act as a strict boundary for the subnet.

## 📸 Verification
<img width="1480" height="286" alt="Screenshot 2025-12-28 at 5 02 48 PM" src="https://github.com/user-attachments/assets/4f5b43d3-0457-442d-bd0d-beadba7960b5" /><br>


1.  **Routing Table Proof:** Screenshot shows the absence of an `igw-xxxxx` target, verifying total isolation.
   <img width="1512" height="810" alt="Screenshot 2025-12-28 at 5 28 25 PM" src="https://github.com/user-attachments/assets/40a63253-2ee5-431a-9c9e-7a1cd19a1aba" /><br>

2.  **Subnet Configuration:** Screenshot confirms the specific CIDR block and correct route table association.
   <img width="1512" height="810" alt="Screenshot 2025-12-28 at 5 28 04 PM" src="https://github.com/user-attachments/assets/bbd910e9-ebce-4cbe-8062-a2b7bd41a05c" /><br>

3.  **Security Layer:** Screenshot of the NACL showing the explicit traffic rules.
   <img width="1512" height="810" alt="Screenshot 2025-12-28 at 5 28 45 PM" src="https://github.com/user-attachments/assets/0e885b4b-f125-46e8-8d68-78d872a931ca" /><br>
   

## 🧠 Key Learnings
* **Isolation is Routing:** A subnet is only "private" if its Route Table says so. IP settings alone are not enough.
* **NACL vs. Security Groups:** I learned that Network ACLs act as a "Subnet Firewall" (Stateless), providing an extra layer of security before traffic even reaches the instance.
* **Implicit Associations:** I had to explicitly associate my subnet with the new Route Table to break the link with the VPC's main public table.
