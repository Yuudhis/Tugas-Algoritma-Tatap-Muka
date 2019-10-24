tier_awal = (input("Masukan Tier Awal: "))
tier_akhir = (input("Masukan Tier Akhir: "))
if tier_awal == "grandmaster" and tier_akhir == "epic":
	print("Harga yang harus dibayar adalah: 50000")
elif tier_awal == "epic" and tier_akhir == "legend":
	print("Harga yang harus dibayar adalah: 70000")
elif tier_awal == "legend" and tier_akhir == "mythic":
	print("Harga yang harus dibayar adalah: 90000")
elif tier_awal == "grandmaster" and tier_akhir == "legend":
	print("Harga yang harus dibayar adalah: 60000")
elif tier_awal == "grandmaster" and tier_akhir == "mythic":
	print("Harga yang harus dibayar adalah: 140000")
elif tier_awal == "epic" and tier_akhir == "mythic":
	print("Harga yang harus dibayar adalah: 120000")
