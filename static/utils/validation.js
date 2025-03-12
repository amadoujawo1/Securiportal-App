// static/js/validation.js
class Validation {
    validateReport(formData) {
      const errors = {};
  
      if (!formData.date) {
        errors.date = 'Date is required.';
      }
      if (!formData.refNo) {
        errors.refNo = 'Reference Number is required.';
      }
      if (!formData.supervisor) {
        errors.supervisor = 'Supervisor is required.';
      }
      if (!formData.flight) {
        errors.flight = 'Flight is required.';
      }
      if (!formData.zone) {
        errors.zone = 'Zone is required.';
      }
  
      return errors;
    }
  
    validateIICSGIA(iicsInfant, iicsAdult, iicsTotal, giaInfant, giaAdult, giaTotal) {
      const errors = {};
  
      if (isNaN(iicsInfant) || iicsInfant < 0 || isNaN(iicsAdult) || iicsAdult < 0 || isNaN(iicsTotal) || iicsTotal < 0) {
        errors.iicsValues = 'IICS values must be non-negative numbers.';
      }
  
      if (isNaN(giaInfant) || giaInfant < 0 || isNaN(giaAdult) || giaAdult < 0 || isNaN(giaTotal) || giaTotal < 0) {
        errors.giaValues = 'GIA values must be non-negative numbers.';
      }
  
      if (iicsInfant + iicsAdult !== iicsTotal) {
        errors.iicsTotalMismatch = 'IICS Infant + Adult must equal IICS Total.';
      }
  
      if (giaInfant + giaAdult !== giaTotal) {
        errors.giaTotalMismatch = 'GIA Infant + Adult must equal GIA Total.';
      }
  
      return errors;
    }

    validateDifference(totalAttended, iicsTotal, giaTotal) {
      const errors = {};
  
      if (totalAttended < iicsTotal) {
        errors.giaValues = 'Total Attended cannot be less than IICS Total.';
      }
  
      if (totalAttended < giaTotal) {
        errors.giaValues = 'Total Attended cannot be less than GIA Total.';
      }
  
      return errors;
    }
  }
  
  const validation = new Validation();