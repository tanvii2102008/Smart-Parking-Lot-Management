Create a complete Enterprise Parking Management System as a single-page web application using only HTML, CSS, and Vanilla JavaScript, without using any frameworks or backend. The system should simulate a real-world multi-floor parking facility with a modern and professional admin dashboard. The parking lot should have 3 floors, each containing 20 parking slots, where the first 4 slots on every floor are VIP slots, and each slot has a unique number based on the floor and slot index. Parking slots can be available, occupied, or reserved, and VIP slots should be visually distinct. The application should allow vehicle entry by capturing details such as vehicle number (mandatory), owner name, contact number, vehicle type, VIP option, and reservation time. It should prevent duplicate vehicle entries, assign the nearest available slot based on floor and VIP preference, and add vehicles to a waiting queue when parking is full, giving priority to VIP vehicles. A queue system should track waiting time and automatically assign vehicles when slots become free. Clicking an occupied slot should open an exit and billing modal, calculate parking duration by rounding hours up, apply vehicle-based pricing, process payment, update revenue, and free the slot. The dashboard should display real-time analytics including slot availability, occupancy, VIP usage, queue length, waiting time, and revenue. The system should also maintain a recent activity log, support search and filtering of slots, provide floor navigation tabs, and include an admin settings panel for pricing, VIP configuration, business hours, notifications, and advanced options. Additionally, the system should generate detailed reports that can be exported as JSON and printable HTML (PDF-friendly). All data should be managed using JavaScript objects and arrays, UI updates should be done using DOM manipulation, and the final output should be a single, well-structured, readable HTML file with embedded CSS and JavaScript.


Create a complete Enterprise Parking Management System as a single-page web application using only HTML, CSS, and Vanilla JavaScript (no frameworks, no backend).

The system should simulate a real-world multi-floor parking facility and include a modern, professional admin dashboard UI.

FUNCTIONAL REQUIREMENTS:

1. Parking Lot Structure
- 3 floors
- 20 parking slots per floor
- First 4 slots on each floor must be VIP slots
- Each slot should have a unique slot number (floor + padded index)

2. Parking Slot States
- available
- occupied
- reserved
- VIP slots must be visually distinguishable

3. Vehicle Entry Module
- Input fields:
  - Vehicle Number (required)
  - Owner Name
  - Contact Number
  - Vehicle Type (Car, Bike, SUV, Truck, EV)
  - VIP checkbox
  - Reservation checkbox with datetime input
- Validate duplicate vehicle entries
- Assign nearest available slot based on:
  - Current floor priority
  - VIP preference
- If no slot is available, add vehicle to waiting queue
- VIP vehicles must get queue priority

4. Waiting Queue System
- Maintain a queue for vehicles when parking is full
- Store queue entry time
- Display live queue count and waiting time
- Auto-assign vehicles from queue when a slot becomes available
- VIP slots should prioritize VIP vehicles

5. Exit & Billing System
- Clicking an occupied slot should open a payment modal
- Calculate parking duration using entry timestamp
- Round hours up to the next full hour
- Apply hourly pricing based on vehicle type
- Collect payment and free the slot
- Update total revenue and today’s revenue
- Auto-assign next eligible vehicle from the queue

6. Dashboard & Analytics
- Show real-time statistics:
  - Total slots
  - Available slots
  - Occupied slots
  - VIP utilization
  - Queue length
  - Average wait time
  - Occupancy percentage
  - Today’s revenue
  - Total revenue
- Automatically update stats on every action

7. Activity Log
- Maintain a recent activity log
- Log entries like:
  - Vehicle parked
  - Vehicle exited
  - Slot reserved
  - Auto-assignment from queue
- Display the latest 5 activities

8. Search & Filters
- Search parking slots by vehicle number
- Filter slots by:
  - All
  - Available
  - Occupied
  - VIP only
- Floor-wise navigation tabs

9. Settings Panel (Admin)
- Pricing configuration per vehicle type
- VIP pricing markup
- VIP slots per floor
- Grace period
- Max queue size
- Business hours (including 24/7 mode)
- Notification preferences
- Advanced settings (debug mode, auto backup, facility name)

10. Reports & Data Export
- Generate a detailed report including:
  - Floor-wise occupancy
  - Parked vehicles
  - Revenue breakdown
  - Activity history
- Export report as:
  - JSON file
  - Printable HTML report (PDF-friendly)

11. UI / UX Requirements
- Modern dashboard layout
- Responsive design
- Modals for exit and settings
- Notifications for success, warning, and errors
- Icons and emojis for better UX
- Clean and professional styling

TECHNICAL CONSTRAINTS:
- Use only HTML5, CSS3, and ES6+ JavaScript
- No external libraries or frameworks
- Store all data in JavaScript objects and arrays
- Use modular functions for logic
- Use DOM manipulation for UI updates

OUTPUT FORMAT:
- Provide a single HTML file
- Include embedded CSS and JavaScript
- Code should be readable, well-structured, and commented


Did you use AI?”, 

say: “Yes, I used AI to scaffold the UI and then refined the logic, state handling, and business rules myself.”



# Enterprise Parking Management System 🅿️

A professional, feature-rich parking lot management system with advanced analytics, revenue tracking, and automated operations.

## 🌟 Key Features

### 🚗 Core Parking Management
- **Multi-Floor Support**: 3 floors with 20 slots each (60 total capacity)
- **Smart Slot Assignment**: Automatically assigns nearest available slot
- **VIP Priority System**: Premium slots with exclusive assignment
- **Vehicle Queue Management**: Automatic assignment when slots free up
- **Real-time Occupancy Tracking**: Live updates across all floors

### 💰 Revenue & Payment
- **Dynamic Pricing**: Configurable rates per vehicle type (Car, Bike, SUV, Truck, EV)
- **Automatic Fare Calculation**: Time-based billing with grace periods
- **Payment Processing**: Complete payment modal with detailed breakdowns
- **Revenue Analytics**: Today's revenue, total revenue, per-vehicle averages
- **Revenue by Vehicle Type**: Track earnings by category

### 📊 Advanced Analytics
- **Floor-wise Statistics**: Individual floor occupancy rates
- **Occupancy Trends**: Real-time percentage calculations
- **Queue Analytics**: Wait time tracking and position management
- **Activity Logging**: Complete audit trail of all operations
- **Comprehensive Reports**: Exportable data and PDF generation

### 🔧 System Configuration
- **Customizable Pricing**: Adjust rates for all vehicle types
- **VIP Markup Control**: Set premium percentage for VIP slots
- **Lot Configuration**: Configure VIP slots, grace periods, max queue size
- **Business Hours**: Set opening/closing times or 24/7 operation
- **Notification Settings**: Control alerts for entry/exit/queue
- **Facility Branding**: Custom facility name

### 📈 Reporting & Data
- **PDF Reports**: Professional reports with charts and tables (via Python script)
- **HTML Reports**: Print-ready reports that open in new window
- **Data Export**: JSON export of all parking data
- **Backup/Restore**: Browser storage backup system
- **Sample Data**: Load demo data for testing

### 🎨 Professional UI/UX
- **Glassmorphic Design**: Modern gradient backgrounds with blur effects
- **Color-Coded Slots**: Visual status indicators (green/red/orange/purple)
- **Interactive Grid**: Click slots to exit vehicles
- **Search & Filter**: Find vehicles, filter by status or VIP
- **Floor Switching**: Easy navigation between floors
- **Responsive Layout**: Works on desktop, tablet, and mobile

### ✨ Smart Features
- **Reservation System**: Pre-book slots with expected arrival time
- **Auto-Assignment**: Queue vehicles automatically assigned on exit
- **VIP Matching**: VIP vehicles only assigned to VIP slots
- **Duration Tracking**: Real-time parking duration display
- **Grace Period**: Configurable free time before billing starts
- **Contact Management**: Store owner name and phone number

## 📋 How to Use

### Basic Operations

1. **Park a Vehicle**
   - Enter vehicle number (required)
   - Add owner name and contact (optional)
   - Select vehicle type
   - Check VIP if premium parking needed
   - Click "Assign Parking Slot"

2. **Exit a Vehicle**
   - Click on any occupied slot (red/purple)
   - Review payment details
   - Click "Process Payment & Exit"
   - System automatically assigns queued vehicle if any

3. **Switch Floors**
   - Click Floor 1/2/3 tabs to view different levels
   - Search works across all floors

4. **Search Vehicles**
   - Use search box to find by vehicle number
   - Filter by status (All/Available/Occupied/VIP)

### Advanced Features

#### Generate Reports

**Method 1: HTML Report (Instant)**
1. Click "📊 Report" button
2. New window opens with complete report
3. Click "Print / Save as PDF" to export

**Method 2: Professional PDF (Python Required)**
1. Click "📊 Report" button
2. Downloads `parking_report_data.json`
3. Run: `python3 generate_parking_report.py parking_report_data.json output.pdf`
4. Professional PDF with charts and tables generated

#### Export Data
1. Click "💾 Export" button
2. All data saved as JSON file
3. Includes slots, queue, revenue, settings, activity log

#### Settings Configuration
1. Click "⚙️ Settings" button
2. Adjust any settings:
   - **Pricing**: Hourly rates per vehicle type
   - **VIP Markup**: Premium percentage
   - **Lot Config**: VIP slots, grace period, queue limits
   - **Business Hours**: Operating schedule
   - **Notifications**: Toggle alerts
   - **Facility Name**: Customize branding
3. Click "Save Settings"

#### Data Management
1. **Backup**: Creates local browser backup
2. **Restore**: Recovers from last backup
3. **Clear All**: Reset system (creates backup first)
4. **Load Sample**: Import demo data for testing

### Reservation System
1. Enter vehicle details
2. Check "Pre-booked Reservation"
3. Select expected arrival time
4. System reserves slot (shows orange)
5. Slot held until arrival or manually released

## 🎯 VIP System

### How VIP Works
- First 4 slots on each floor are VIP (101-104, 201-204, 301-304)
- VIP checkbox must be selected for VIP parking
- VIP vehicles ONLY assigned to VIP slots
- Regular vehicles ONLY assigned to regular slots
- Queue respects VIP status (VIP slot → VIP vehicle)
- Purple color indicates VIP slots

### VIP Benefits
- Guaranteed slot availability (dedicated)
- Premium positioning (near entrance)
- Priority in queue
- Custom markup pricing

## 💾 Data Persistence

All data is stored in browser localStorage:
- Settings are saved automatically
- Create backups before clearing data
- Export to JSON for external storage
- Use Python script for archival PDF reports

## 🔒 Security & Privacy

- All data stored locally in browser
- No external server communication
- Owner/contact info optional
- Activity log for audit trail
- Settings protected by confirmation dialogs

## 📊 Report Contents

### Executive Summary
- Total/Occupied/Available slots
- Queue length
- Occupancy rate
- Revenue (today & total)

### Floor-wise Analysis
- Per-floor occupancy
- VIP slot utilization
- Availability percentages

### Vehicle Details
- All parked vehicles
- Entry times & durations
- Owner information
- Slot assignments

### Revenue Breakdown
- Total revenue
- By vehicle type
- Average per transaction
- Today vs all-time

### Activity Log
- Recent operations
- Timestamped entries
- Entry/exit records
- Payment transactions

## 🛠️ Technical Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Design**: Glassmorphism, CSS Grid, Flexbox
- **Storage**: localStorage API
- **Reports**: ReportLab (Python) for PDF
- **Icons**: Unicode emoji

## 📱 Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Responsive

## 🚀 Quick Start

1. Open `enterprise-parking-system.html`
2. Click "Load Sample" in settings for demo data
3. Explore features with pre-populated vehicles
4. Click "Clear All Data" to start fresh

## 💡 Tips & Tricks

- **Keyboard shortcuts**: Tab to navigate form fields
- **Click slots**: Fastest way to exit vehicles
- **Floor tabs**: Remember which floor you're on
- **Search**: Works across all floors simultaneously
- **Filters**: Combine with search for precision
- **Debug mode**: Enable in settings to see console logs
- **Backup often**: Before making major changes
- **Export regularly**: Keep JSON archives

## 📞 Support

For issues or feature requests:
1. Check browser console for errors (F12)
2. Enable debug mode in settings
3. Export data before troubleshooting
4. Review activity log for operation history

## 🔄 Version History

**v1.0** - Initial Release
- Multi-floor parking management
- VIP system
- Revenue tracking
- Queue management
- Settings panel
- Report generation
- Data export/backup

---

**Built with ❤️ for professional parking operations**
