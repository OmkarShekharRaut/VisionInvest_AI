// controllers/authController.js
const { generateMFASecret, verifyMFA } = require("../services/mfaService");
const { sendOTPEmail } = require("../services/emailService");

/**
 * Enable MFA for a user
 */
exports.enableMFA = async (req, res) => {
    const { email } = req.body;

    try {
        const secretURL = await generateMFASecret(email);
        res.json({ message: "MFA Enabled!", secretURL });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

/**
 * Send OTP to user's email
 */
exports.sendOTP = async (req, res) => {
    const { email } = req.body;
    const otp = Math.floor(100000 + Math.random() * 900000).toString(); // Generate 6-digit OTP

    try {
        await sendOTPEmail(email, otp);
        res.json({ message: "OTP Sent!" });
    } catch (error) {
        res.status(500).json({ error: "Failed to send OTP" });
    }
};

/**
 * Verify OTP for MFA
 */
exports.verifyOTP = async (req, res) => {
    const { email, token } = req.body;

    try {
        const isValid = await verifyMFA(email, token);
        if (isValid) {
            res.json({ message: "MFA Verified!" });
        } else {
            res.status(400).json({ error: "Invalid OTP" });
        }
    } catch (error) {
        res.status(500).json({ error: "OTP verification failed" });
    }
};
