# Configuración de nodos
### DNS: 
```json
{
    "compute_id": "local",
    "console": 5000,
    "console_auto_start": true,
    "console_type": "telnet",
    "custom_adapters": [],
    "first_port_name": null,
    "height": 70,
    "label": {
        "rotation": 0,
        "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
        "text": "DNS-1",
        "x": -2,
        "y": -25
    },
    "locked": false,
    "name": "DNS-1",
    "node_id": "2610c969-3da7-49d4-92c7-a6286d80faef",
    "node_type": "docker",
    "port_name_format": "Ethernet{0}",
    "port_segment_size": 0,
    "properties": {
        "adapters": 1,
        "aux": 5001,
        "console_http_path": "/",
        "console_http_port": 80,
        "console_resolution": "800x600",
        "container_id": "cd6ac2e1f58382a0e307ac82799340254b833e710d04c6a578e30d151385759a",
        "environment": "MAC=0\nTYPE=1",
        "extra_hosts": null,
        "extra_volumes": [
            "/etc",
            "/var/cache/bind"
        ],
        "image": "jcfabero/server:latest",
        "start_command": "/bin/bash",
        "usage": "Configure bind9 in /etc/bind\nNetwork can be configured with DHCP via %dhclient -v eth0%"
    },
    "symbol": ":/symbols/classic/server.svg",
    "template_id": "fd0fc58f-b0f9-4516-b431-b297339d6b4f",
    "width": 49,
    "x": -249,
    "y": -38,
    "z": 1
}
```
### SWITCH:
```json
{
"compute_id": "local",
"console": 5004,
"console_auto_start": false,
"console_type": "none",
"custom_adapters": [],
"first_port_name": null,
"height": 32,
"label": {
    "rotation": 0,
    "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
    "text": "Switch1",
    "x": 2,
    "y": -25
},
"locked": false,
"name": "Switch1",
"node_id": "c3d615b1-20bb-441e-b710-e997b35ac830",
"node_type": "ethernet_switch",
"port_name_format": "Ethernet{0}",
"port_segment_size": 0,
"properties": {
    "ports_mapping": [
        {
            "name": "Ethernet0",
            "port_number": 0,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet1",
            "port_number": 1,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet2",
            "port_number": 2,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet3",
            "port_number": 3,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet4",
            "port_number": 4,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet5",
            "port_number": 5,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet6",
            "port_number": 6,
            "type": "access",
            "vlan": 1
        },
        {
            "name": "Ethernet7",
            "port_number": 7,
            "type": "access",
            "vlan": 1
        }
    ]
},
"symbol": ":/symbols/ethernet_switch.svg",
"template_id": "1966b864-93e7-32d5-965f-001384eec461",
"width": 72,
"x": -147,
"y": -161,
"z": 1
}
```
### ROUTER:
```json
{
    "compute_id": "local",
    "console": 5005,
    "console_auto_start": true,
    "console_type": "telnet",
    "custom_adapters": [],
    "first_port_name": null,
    "height": 45,
    "label": {
        "rotation": 0,
        "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
        "text": "FRR-1",
        "x": 7,
        "y": -25
    },
    "locked": false,
    "name": "FRR-1",
    "node_id": "5053fd90-39a6-4b4d-bfb4-6eb7219c3d31",
    "node_type": "docker",
    "port_name_format": "Ethernet{0}",
    "port_segment_size": 0,
    "properties": {
        "adapters": 8,
        "aux": 5006,
        "console_http_path": "/",
        "console_http_port": 80,
        "console_resolution": "800x600",
        "container_id": "a6d61442e5256bfbfd61d121eac14385bef724de2d5a462bc4de989324ed2199",
        "environment": "MAC=0\nTYPE=2",
        "extra_hosts": null,
        "extra_volumes": [
            "/etc"
        ],
        "image": "jcfabero/frr-dhcp:latest",
        "start_command": "zebra.sh",
        "usage": "Configure frr with \"vtysh\", dhcpd in \"/etc/dhcp/dhcpd.conf\" and nftables in \"/etc/nftables\"."
    },
    "symbol": ":/symbols/classic/router_firewall.svg",
    "template_id": "f5731593-4473-49af-bc6d-a7e9e8d552fa",
    "width": 66,
    "x": -57,
    "y": -79,
    "z": 1
}
```

# Configuración de links
### DNS &harr; SWITCH
```json
{
    "filters": {},
    "link_id": "1942959d-ff30-4aea-afde-1b54bd93b12d",
    "link_style": {},
    "nodes": [
        {
            "adapter_number": 0,
            "label": {
                "rotation": 0,
                "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
                "text": "eth0",
                "x": 50,
                "y": 3
            },
            "node_id": "2610c969-3da7-49d4-92c7-a6286d80faef",
            "port_number": 0
        },
        {
            "adapter_number": 0,
            "label": {
                "rotation": 0,
                "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
                "text": "e0",
                "x": 9,
                "y": 46
            },
            "node_id": "c3d615b1-20bb-441e-b710-e997b35ac830",
            "port_number": 0
        }
    ],
    "suspend": false
}
```
### DNS &harr; ROUTER
```json
{
    "filters": {},
    "link_id": "cbff4034-53ce-4718-a7c6-08bab55a4bde",
    "link_style": {},
    "nodes": [
        {
            "adapter_number": 0,
            "label": {
                "rotation": 0,
                "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
                "text": "eth0",
                "x": 64,
                "y": 35
            },
            "node_id": "05303dfb-5b09-494d-8be2-a31032fa9076",
            "port_number": 0
        },
        {
            "adapter_number": 0,
            "label": {
                "rotation": 0,
                "style": "font-family: TypeWriter;font-size: 10.0;font-weight: bold;fill: #000000;fill-opacity: 1.0;",
                "text": "eth0",
                "x": -6,
                "y": 21
            },
            "node_id": "5053fd90-39a6-4b4d-bfb4-6eb7219c3d31",
            "port_number": 0
        }
    ],
    "suspend": false
}
```