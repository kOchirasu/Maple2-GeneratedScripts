using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000669: Ronzo
/// </summary>
public class _11000669 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002718$
    // - WHAT?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002721$
                // - What are you doing here? How did you even GET here?
                switch (selection) {
                    // $script:0831180407002722$
                    // - Easily.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002723$
                // - Kid, I'm impressed. You made it this far, but it's time for you to go. Leave before something bad happens to you. 
                switch (selection) {
                    // $script:0831180407002724$
                    // - Why?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0831180407002725$
                // - I stay well away from the basement levels. And I live here!
                return 32;
            case (32, 1):
                // $script:0831180407002726$
                // - I had to come down here today, but believe me... I can't WAIT to get back upstairs.
                return 32;
            case (32, 2):
                // $script:0831180407002727$
                // - Don't try anything stupid. Just get out of here!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Next,
            (32, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
