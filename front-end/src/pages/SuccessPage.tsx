import React from "react";

type SuccessPageProps = {
  onClose: () => void;
};

const SuccessPage: React.FC<SuccessPageProps> = ({ onClose }) => {
  return (
    <div>
      <h1>Payment Successful!</h1>
      <p>Thank you for your purchase.</p>
      <button onClick={onClose}>Close</button>
    </div>
  );
};

export default SuccessPage;
