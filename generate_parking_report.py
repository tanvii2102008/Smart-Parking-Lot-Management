#!/usr/bin/env python3
"""
Parking Management System - Report Generator
Generates comprehensive PDF reports with parking statistics, revenue, and activity logs
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from datetime import datetime
import json
import sys

def create_header(canvas, doc, facility_name):
    """Create header for each page"""
    canvas.saveState()
    
    # Header background
    canvas.setFillColor(colors.HexColor('#667eea'))
    canvas.rect(0, letter[1] - 80, letter[0], 80, fill=1, stroke=0)
    
    # Title
    canvas.setFillColor(colors.white)
    canvas.setFont('Helvetica-Bold', 24)
    canvas.drawString(50, letter[1] - 45, f"🅿️ {facility_name}")
    
    canvas.setFont('Helvetica', 12)
    canvas.drawString(50, letter[1] - 65, "Parking Management Report")
    
    # Date on right
    canvas.setFont('Helvetica', 10)
    canvas.drawRightString(letter[0] - 50, letter[1] - 45, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    canvas.restoreState()

def create_footer(canvas, doc):
    """Create footer for each page"""
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawCentredString(letter[0] / 2, 30, f"Page {doc.page}")
    canvas.drawRightString(letter[0] - 50, 30, "Enterprise Parking System")
    canvas.restoreState()

def generate_parking_report(data, output_file="parking_report.pdf"):
    """
    Generate comprehensive parking report PDF
    
    Args:
        data: Dictionary containing parking data
        output_file: Output PDF filename
    """
    
    # Create document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=100,
        bottomMargin=50
    )
    
    # Container for content
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    # Report Title
    story.append(Paragraph("PARKING OPERATIONS REPORT", title_style))
    story.append(Spacer(1, 20))
    
    # Executive Summary
    story.append(Paragraph("Executive Summary", heading_style))
    
    summary_data = [
        ['Metric', 'Value'],
        ['Total Slots', str(data.get('totalSlots', 0))],
        ['Currently Occupied', str(data.get('occupied', 0))],
        ['Currently Available', str(data.get('available', 0))],
        ['Vehicles in Queue', str(data.get('queueLength', 0))],
        ['Occupancy Rate', f"{data.get('occupancyRate', 0)}%"],
        ['Today\'s Revenue', f"${data.get('todayRevenue', 0):.2f}"],
        ['Total Revenue', f"${data.get('totalRevenue', 0):.2f}"],
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))
    
    story.append(summary_table)
    story.append(Spacer(1, 30))
    
    # Floor-wise Analysis
    if 'floors' in data:
        story.append(Paragraph("Floor-wise Occupancy", heading_style))
        
        floor_data = [['Floor', 'Total Slots', 'Occupied', 'Available', 'VIP Slots', 'Occupancy %']]
        for floor in data['floors']:
            floor_data.append([
                f"Floor {floor['number']}",
                str(floor['total']),
                str(floor['occupied']),
                str(floor['available']),
                str(floor['vip']),
                f"{floor['occupancy']}%"
            ])
        
        floor_table = Table(floor_data, colWidths=[1*inch, 1.2*inch, 1*inch, 1*inch, 1*inch, 1.2*inch])
        floor_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8b5cf6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ]))
        
        story.append(floor_table)
        story.append(Spacer(1, 30))
    
    # Currently Parked Vehicles
    if 'parkedVehicles' in data and data['parkedVehicles']:
        story.append(Paragraph("Currently Parked Vehicles", heading_style))
        
        vehicle_data = [['Slot', 'Vehicle Number', 'Type', 'Owner', 'Entry Time', 'Duration']]
        for vehicle in data['parkedVehicles'][:20]:  # Limit to 20 for space
            vehicle_data.append([
                vehicle.get('slot', 'N/A'),
                vehicle.get('number', 'N/A'),
                vehicle.get('type', 'N/A'),
                vehicle.get('owner', 'N/A'),
                vehicle.get('entryTime', 'N/A'),
                vehicle.get('duration', 'N/A')
            ])
        
        vehicle_table = Table(vehicle_data, colWidths=[0.7*inch, 1.3*inch, 0.8*inch, 1.2*inch, 1.3*inch, 0.9*inch])
        vehicle_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10b981')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ]))
        
        story.append(vehicle_table)
        story.append(Spacer(1, 30))
    
    # Page break before next section
    story.append(PageBreak())
    
    # Revenue Analysis
    story.append(Paragraph("Revenue Analysis", heading_style))
    
    revenue_data = [
        ['Category', 'Amount'],
        ['Today\'s Revenue', f"${data.get('todayRevenue', 0):.2f}"],
        ['Total Revenue (All Time)', f"${data.get('totalRevenue', 0):.2f}"],
        ['Average Revenue per Vehicle', f"${data.get('avgRevenue', 0):.2f}"],
    ]
    
    if 'revenueByType' in data:
        revenue_data.append(['Revenue by Vehicle Type', ''])
        for vtype, amount in data['revenueByType'].items():
            revenue_data.append([f"  {vtype}", f"${amount:.2f}"])
    
    revenue_table = Table(revenue_data, colWidths=[3*inch, 2*inch])
    revenue_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f59e0b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))
    
    story.append(revenue_table)
    story.append(Spacer(1, 30))
    
    # Activity Log
    if 'activityLog' in data and data['activityLog']:
        story.append(Paragraph("Recent Activity Log", heading_style))
        
        activity_data = [['Time', 'Activity']]
        for activity in data['activityLog'][-15:]:  # Last 15 activities
            activity_data.append([
                activity.get('time', 'N/A'),
                activity.get('text', 'N/A')
            ])
        
        activity_table = Table(activity_data, colWidths=[2*inch, 4.5*inch])
        activity_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('TOPPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ]))
        
        story.append(activity_table)
    
    # Footer note
    story.append(Spacer(1, 40))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    story.append(Paragraph(
        "This is an automated report generated by the Enterprise Parking Management System.<br/>"
        "For questions or support, please contact your system administrator.",
        footer_style
    ))
    
    # Build PDF with header and footer
    doc.build(
        story,
        onFirstPage=lambda c, d: (create_header(c, d, data.get('facilityName', 'Enterprise Parking System')), create_footer(c, d)),
        onLaterPages=lambda c, d: (create_header(c, d, data.get('facilityName', 'Enterprise Parking System')), create_footer(c, d))
    )
    
    return output_file

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        # Read data from file
        with open(sys.argv[1], 'r') as f:
            data = json.load(f)
    else:
        # Sample data for testing
        data = {
            'facilityName': 'Enterprise Parking System',
            'timestamp': datetime.now().isoformat(),
            'totalSlots': 60,
            'occupied': 35,
            'available': 25,
            'queueLength': 5,
            'occupancyRate': 58,
            'todayRevenue': 450.50,
            'totalRevenue': 12850.75,
            'avgRevenue': 12.50,
            'floors': [
                {'number': 1, 'total': 20, 'occupied': 12, 'available': 8, 'vip': 4, 'occupancy': 60},
                {'number': 2, 'total': 20, 'occupied': 15, 'available': 5, 'vip': 4, 'occupancy': 75},
                {'number': 3, 'total': 20, 'occupied': 8, 'available': 12, 'vip': 4, 'occupancy': 40},
            ],
            'parkedVehicles': [
                {'slot': '101', 'number': 'MH-12-AB-1234', 'type': 'Car', 'owner': 'John Doe', 'entryTime': '10:30 AM', 'duration': '2h 30m'},
                {'slot': '105', 'number': 'DL-05-XY-5678', 'type': 'SUV', 'owner': 'Jane Smith', 'entryTime': '11:15 AM', 'duration': '1h 45m'},
            ],
            'revenueByType': {
                'Car': 250.00,
                'SUV': 150.50,
                'Bike': 30.00,
                'Truck': 20.00
            },
            'activityLog': [
                {'time': '13:45', 'text': 'MH-12-AB-1234 parked in slot 101'},
                {'time': '13:50', 'text': 'DL-05-XY-5678 parked in slot 105'},
                {'time': '14:00', 'text': 'KA-03-CD-9012 exited from slot 203'},
            ]
        }
    
    output_file = sys.argv[2] if len(sys.argv) > 2 else '/mnt/user-data/outputs/parking_report.pdf'
    
    print(f"Generating report: {output_file}")
    generate_parking_report(data, output_file)
    print(f"Report generated successfully: {output_file}")
