using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000503: Armano
/// </summary>
public class _11000503 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002184$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002185$
                // - Ah, $MyPCName$! Good to see you again. I made it home safely, all thanks to you. I thought Dad would be mad, but he let me in without saying a word. 
                return 10;
            case (10, 1):
                // $script:0831180407002186$
                // - I've decided to stay out of trouble and be good. Come back and visit, will you?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
