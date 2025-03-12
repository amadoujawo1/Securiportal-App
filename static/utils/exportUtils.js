// static/js/exportUtils.js
class ExportUtils {
    exportToCSV(data) {
      if (!data || data.length === 0) {
        alert('No data to export.');
        return;
      }
  
      const csvRows = [];
      const headers = Object.keys(data[0]);
      csvRows.push(headers.join(','));
  
      for (const row of data) {
        const values = headers.map(header => {
          let value = row[header];
          if (typeof value === 'string') {
            value = value.replace(/"/g, '""'); // Escape double quotes
            return `"${value}"`; // Wrap in double quotes
          }
          return value;
        });
        csvRows.push(values.join(','));
      }
  
      const csvData = csvRows.join('\n');
      const blob = new Blob([csvData], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'data.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
  
  const exportUtils = new ExportUtils();