(function ($) {
  $(document).ready(function () {
    function updateRoundChoices() {
      var investmentType = $("#id_investment_type").val();
      var roundField = $("#id_round");
      var choices = [];

      if (investmentType === "Startup") {
        choices = [
          ["Seed", "Seed"],
          ["Series 1", "Series 1"],
          ["Series 2", "Series 2"],
          ["Series 3", "Series 3"],
          ["IPO", "IPO"],
        ];
      } else if (investmentType === "Innovation") {
        choices = [
          ["Concept", "Concept"],
          ["Prototype", "Prototype"],
          ["Development", "Development"],
          ["Deployed", "Deployed"],
        ];
      }

      roundField.empty();
      $.each(choices, function (index, choice) {
        roundField.append(new Option(choice[1], choice[0]));
      });
    }

    // Bind the function to the change event of the investment_type field
    $("#id_investment_type").change(updateRoundChoices);
    // Initialize the choices on page load
    updateRoundChoices();
  });
})(django.jQuery);
