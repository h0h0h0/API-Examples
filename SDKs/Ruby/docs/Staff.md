# SwaggerClient::Staff

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The address of the staff member who is teaching the class. | [optional] 
**appointment_instructor** | **BOOLEAN** | When &#x60;true&#x60;, indicates that the staff member offers appointments.&lt;br /&gt;  When &#x60;false&#x60;, indicates that the staff member does not offer appointments. | [optional] 
**always_allow_double_booking** | **BOOLEAN** | When &#x60;true&#x60;, indicates that the staff member can be scheduled for overlapping services.&lt;br /&gt;  When &#x60;false&#x60;, indicates that the staff can only be scheduled for one service at a time in any given time-frame. | [optional] 
**bio** | **String** | The staff member’s biography. This string contains HTML. | [optional] 
**city** | **String** | The staff member’s city. | [optional] 
**country** | **String** | The staff member’s country. | [optional] 
**email** | **String** | The staff member’s email address. | [optional] 
**first_name** | **String** | The staff member’s first name. | [optional] 
**home_phone** | **String** | The staff member’s home phone number. | [optional] 
**id** | **Integer** | The ID assigned to the staff member. | [optional] 
**independent_contractor** | **BOOLEAN** | When &#x60;true&#x60;, indicates that the staff member is an independent contractor.  When &#x60;false&#x60;, indicates that the staff member is not an independent contractor. | [optional] 
**is_male** | **BOOLEAN** | When &#x60;true&#x60;, indicates that the staff member is male.  When &#x60;false&#x60;, indicates that the staff member is female. | [optional] 
**last_name** | **String** | The staff member’s last name. | [optional] 
**mobile_phone** | **String** | The staff member’s mobile phone number. | [optional] 
**name** | **String** | The staff member’s name. | [optional] 
**postal_code** | **String** | The staff member’s postal code. | [optional] 
**class_teacher** | **BOOLEAN** | When &#x60;true&#x60;, indicates that the staff member can teach classes.  When &#x60;false&#x60;, indicates that the staff member cannot teach classes. | [optional] 
**sort_order** | **Integer** | If configured by the business owner, this field determines a staff member’s weight when sorting. Use this field to sort staff members on your interface. | [optional] 
**state** | **String** | The staff member’s state. | [optional] 
**work_phone** | **String** | The staff member’s work phone number. | [optional] 
**image_url** | **String** | The URL of the staff member’s image, if one has been uploaded. | [optional] 
**appointments** | [**Array&lt;Appointment&gt;**](Appointment.md) | A list of appointments for the staff. | [optional] 
**unavailabilities** | [**Array&lt;Unavailability&gt;**](Unavailability.md) | A list of unavailabilities for the staff. | [optional] 
**availabilities** | [**Array&lt;Availability&gt;**](Availability.md) | A list of availabilities for the staff. | [optional] 


