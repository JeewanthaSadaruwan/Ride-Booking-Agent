# Testing the Authentication System

## Quick Test Guide

### 1. Start the Application
```bash
cd "/home/jeewanthas/Desktop/ride booking agent"
streamlit run app.py
```

Open your browser to: **http://localhost:8501**

### 2. Create a Test Account

**Click "Create Account" and fill in:**
- Full Name: `Test User`
- Email: `test@example.com`
- Phone: `0771234567` or `+94771234567`
- Password: `test123` (minimum 6 characters)
- Confirm Password: `test123`

Click "Create Account" ✅

### 3. Login

**After account creation:**
- Email: `test@example.com`
- Password: `test123`

Click "Login" 🚀

### 4. Explore Features

#### Check Your Profile (Sidebar)
- See your name, email, phone
- View your stats (Total Bookings, Completed, Total Spent)
- Click "Logout" to test logout

#### Book a Ride (Tab 1: 💬 Book a Ride)
Try these test queries:

```
"Hello, I need a ride from Gampaha to Colombo Fort"
```

The agent should:
- Greet you by name: "Welcome back, Test User!" or "Hello, Test User!"
- Confirm locations
- Ask for passenger count
- Ask for pickup time
- Show vehicle options with prices
- Ask for confirmation
- Complete the booking

**Complete Booking Flow:**
1. "I need a ride from Colombo to Kandy"
2. Agent asks: "How many passengers?"
3. You: "2 passengers"
4. Agent asks: "When would you like the pickup?"
5. You: "Tomorrow at 10 AM"
6. Agent shows 3 vehicle options with prices
7. You: "I'll take option 2"
8. Agent shows booking summary
9. You: "Yes, confirm"
10. Agent books and shows confirmation with booking ID

#### View Booking History (Tab 2: 📋 My Bookings)
- Click the "📋 My Bookings" tab
- See all your bookings
- Expand any booking to see details
- Try cancelling a confirmed booking

### 5. Test Multiple Users

**Create a second account:**
- Logout
- Create new account with different email
- Login with second account
- Book a ride
- Notice: Each user has separate booking history!

### 6. Test Personalization

**With User 1 logged in:**
```
"What is the time now"
```
Agent should: Call the tool and give current time

```
"Book another ride from Negombo to Airport"
```
Agent should: Greet you by name and process the booking

### 7. Test Validation

**Try invalid inputs during signup:**

❌ Invalid Email:
- Email: `notanemail`
- Should show: "Invalid email format"

❌ Short Password:
- Password: `123`
- Should show: "Password must be at least 6 characters"

❌ Invalid Phone:
- Phone: `123`
- Should show: "Invalid phone number format"

❌ Duplicate Email:
- Try signing up with same email twice
- Should show: "Email already registered"

### 8. Test Profile Stats

**After booking 2-3 rides:**
- Check sidebar
- Total Bookings should increase
- Total Spent should show sum of booking costs

### 9. Test Booking Cancellation

**In Booking History tab:**
1. Find a confirmed booking
2. Click "Cancel Booking" button
3. Booking status should change to "cancelled"
4. Completed bookings count should not decrease

## Expected Behavior

✅ **Authentication Works:**
- Users can signup, login, logout
- Passwords are hashed and secure
- Session persists during browsing
- Logout clears session

✅ **Personalization Works:**
- Agent greets users by name
- User context is passed to agent
- Bookings are linked to user accounts

✅ **Booking History Works:**
- All bookings are saved
- Users can view their history
- Booking details are complete
- Status tracking works

✅ **Stats Work:**
- Total bookings count increases
- Completed bookings tracked
- Total spent calculates correctly

## Test Scenarios

### Scenario 1: First-Time User Journey
1. Open app → See login
2. Create account
3. Login
4. See welcome message
5. Book first ride
6. Check booking history
7. Logout

### Scenario 2: Returning User Journey
1. Open app → See login
2. Login with existing account
3. See "Welcome back, [Name]!"
4. View past bookings
5. Book new ride
6. See updated stats

### Scenario 3: Multiple Bookings
1. Login
2. Book ride: Colombo → Kandy
3. Book ride: Gampaha → Negombo
4. Book ride: Negombo → Airport
5. Check history → See 3 bookings
6. Check stats → Total bookings: 3

### Scenario 4: Booking Management
1. Login
2. Book 2 rides
3. View booking history
4. Cancel 1 booking
5. Verify: Cancelled booking shows ❌ status
6. Stats: Cancelled booking not counted in completed

## Common Issues & Solutions

### Issue: "Email already registered"
**Solution:** Use a different email or login with existing account

### Issue: Can't login
**Solution:** 
- Check email spelling
- Verify password is correct
- Try "Create Account" if you haven't registered

### Issue: Booking not showing in history
**Solution:** 
- Ensure you completed the full booking flow
- Check that you confirmed the booking
- Refresh the page

### Issue: Stats not updating
**Solution:** 
- Complete the full booking process
- Refresh the page
- Check "📋 My Bookings" tab

## Database Location

The database is stored at:
```
/home/jeewanthas/Desktop/ride booking agent/vehicles.db
```

To reset everything:
```bash
rm vehicles.db
# Restart the app - it will recreate the database
```

## Success Criteria

✅ You should be able to:
1. Create an account
2. Login and see your name in sidebar
3. Book a ride with personalized agent interaction
4. View booking history with all details
5. See accurate statistics
6. Cancel bookings
7. Logout and login again
8. Create multiple accounts with separate data

---

**Happy Testing!** 🎉🚗
