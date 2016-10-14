$TTL	315360000
@	IN	SOA	be.	admin.be.(
	1	; Serial
	604800	; Refresh
	86400	; Retry
	315360000	; Expire
	604800)	; Negative Cache TTL

; name server - NS records
	NS	ns.be.

; name server - A records
ns.be.	IN	A	10.10.0.1

; 10.10.0.0/16 - A records
entertainment.be.	IN	A	10.10.0.1
