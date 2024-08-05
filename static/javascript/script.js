$(document).ready(function(){
    $('#myForm').on('submit', function(e){
        e.preventDefault(); // Prevent the default form submission
        
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(), // Serialize the form data
            dataType: 'json',
            success: function(response){
                if(response.success){
                    $('#successModal').modal('show'); // Show the modal
                    $('#myForm')[0].reset(); // Reset the form fields
                } else {
                    alert('There was an error sending your message. Please try again.');
                }
            },
            error: function(xhr){
                // Handle server errors (status code 400 or 500)
                if(xhr.status === 400){
                    let errors = xhr.responseJSON.errors;
                    let errorMessage = 'Please correct the following errors:\n';
                    for (let field in errors) {
                        errorMessage += `${field}: ${errors[field]}\n`;
                    }
                    alert(errorMessage);
                } else {
                    alert('An unexpected error occurred. Please try again later.');
                }
            }
        });
    });
});