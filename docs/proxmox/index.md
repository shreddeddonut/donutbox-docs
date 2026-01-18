# Proxmox

Notes for building, maintaining, and troubleshooting Proxmox VE clusters and VMs/CTs.

## Core topics
- Storage: ZFS, LVM-thin, Ceph (if used), backups, pruning
- Networking: bridges, VLANs, firewall rules, SDN
- Virtualization: VM vs LXC, virtio, CPU types, PCIe passthrough
- Backups: Proxmox Backup Server, schedules, retention, restores

## Common workflows
- Create a VM template (cloud-init)
- Add VLAN-aware bridges
- GPU/iGPU passthrough checks (IOMMU, vfio, ROMs)
- Snapshot + rollback before upgrades

## Useful pages
- Build checklist
- Networking
- Storage & ZFS
- Passthrough
- Backups

> Tip: Include exact commands + the expected output (or “what good looks like”).