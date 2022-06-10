using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004288: MC Nagi
/// </summary>
public class _11004288 : NpcScript {
    internal _11004288(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0218154407014479$ 
                // - I'm MC Nagi, your host in the Queen Bean Rumble! 
                return true;
            case 10:
                // $script:0218154407014480$ 
                // - Welcome to the rumble! You look like you're ready to get wild. 
                // $script:0226180207014575$ 
                // - Let's start the match! 
                switch (selection) {
                    // $script:0226181607014578$
                    // - I'm ready.
                    case 0:
                        Id = 0; // TODO: 20 | 60
                        return false;
                }
                return true;
            case 20:
                // $script:0218154407014481$ 
                // - So, what are we doing today? 
                switch (selection) {
                    // $script:0218154407014482$
                    // - Start Over
                    case 0:
                        Id = 30;
                        return false;
                    // $script:0218154407014483$
                    // - Continue
                    case 1:
                        Id = 0; // TODO: 40 | 50
                        return false;
                }
                return true;
            case 30:
                // $script:0218154407014484$ functionID=1 
                // - Taking it from the top, eh? Exciting! Now, let's get to it! 
                return true;
            case 40:
                // $script:0218154407014485$ functionID=2 
                // - You already beat everyone, ya goof! Why don't we start over, instead? 
                return true;
            case 50:
                // $script:0226191507014580$ functionID=3 
                // - Great! Keep up that fighting spirit! Now start! 
                return true;
            case 60:
                // $script:0226191507014581$ functionID=4 
                // - Here's your first challenge. Good luck! 
                return true;
            default:
                return true;
        }
    }
}
