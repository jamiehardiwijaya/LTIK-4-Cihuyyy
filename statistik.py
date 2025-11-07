# Fitur Statistik Food Waste Management System

def calculate_average_waste(waste_data):
    if not waste_data:
        return 0.0
    total_waste = sum(waste_data)
    average_waste = total_waste / len(waste_data)
    return average_waste

def calculate_total_waste(waste_data):
    total_waste = sum(waste_data)
    return total_waste

def calculate_waste_trend(waste_data):
    if len(waste_data) < 2:
        return 'stable'
    
    if waste_data[-1] > waste_data[0]:
        return 'increasing'
    elif waste_data[-1] < waste_data[0]:
        return 'decreasing'
    else:
        return 'stable'
    
def generate_waste_report(waste_data):
    report = {
        'average_waste': calculate_average_waste(waste_data),
        'total_waste': calculate_total_waste(waste_data),
        'waste_trend': calculate_waste_trend(waste_data)
    }
    return report

if __name__ == "__main__":
    sample_waste_data = [10.5, 12.0, 9.8, 11.2, 13.5]
    report = generate_waste_report(sample_waste_data)
    print("Laporan Statistik Sampah Makanan:")
    print(f"Rata-rata Sampah: {report['average_waste']} kg")
    print(f"Total Sampah: {report['total_waste']} kg")
    print(f"Tren Sampah: {report['waste_trend']}")
