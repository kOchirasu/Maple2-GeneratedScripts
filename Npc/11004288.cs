using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004288: MC Nagi
/// </summary>
public class _11004288 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0218154407014479$
    // - I'm MC Nagi, your host in the Queen Bean Rumble!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0218154407014480$
                // - Welcome to the rumble! You look like you're ready to get wild.
                return 10;
            case (10, 1):
                // $script:0226180207014575$
                // - Let's start the match!
                switch (selection) {
                    // $script:0226181607014578$
                    // - I'm ready.
                    case 0:
                        // TODO: goto 20
                        // TODO: gotoFail 60
                        return -1;
                }
                return -1;
            case (20, 0):
                // $script:0218154407014481$
                // - So, what are we doing today?
                switch (selection) {
                    // $script:0218154407014482$
                    // - Start Over
                    case 0:
                        return 30;
                    // $script:0218154407014483$
                    // - Continue
                    case 1:
                        // TODO: goto 40
                        // TODO: gotoFail 50
                        return -1;
                }
                return -1;
            case (30, 0):
                // functionID=1 
                // $script:0218154407014484$
                // - Taking it from the top, eh? Exciting! Now, let's get to it!
                return -1;
            case (40, 0):
                // functionID=2 
                // $script:0218154407014485$
                // - You already beat everyone, ya goof! Why don't we start over, instead?
                return -1;
            case (50, 0):
                // functionID=3 
                // $script:0226191507014580$
                // - Great! Keep up that fighting spirit! Now start!
                return -1;
            case (60, 0):
                // functionID=4 
                // $script:0226191507014581$
                // - Here's your first challenge. Good luck!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
