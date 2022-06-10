using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001671: Junta
/// </summary>
public class _11001671 : NpcScript {
    internal _11001671(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0711210007006721$ 
                // - You have something to say to me? 
                return true;
            case 30:
                // $script:0727223007006884$ 
                // - If you have something to say, just say it. 
                switch (selection) {
                    // $script:0727223007006885$
                    // - Where have you been?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0727223007006886$
                    // - You're hurt.
                    case 1:
                        Id = 50;
                        return false;
                    // $script:0727223007006887$
                    // - What are these shadows?
                    case 2:
                        Id = 60;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006888$ 
                // - As I said, I saw one of those creatures while checking on the barrier stones. It led me into a trap, which took time to get myself out of. Do not worry... those who laid the trap will be laying no others. 
                switch (selection) {
                    // $script:0727233607006924$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 50:
                // $script:0727223007006889$ 
                // - Do not presume to tell me my business! I am the first student of Guidance, and those frail things could hardly lay a... a... whatever they have on me! 
                switch (selection) {
                    // $script:0727233607006925$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 60:
                // $script:0727223007006890$ 
                // - I have no idea. They aren't of nature, that much is obvious. And they are organized. Someone is behind this... 
                switch (selection) {
                    // $script:0727233607006926$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
