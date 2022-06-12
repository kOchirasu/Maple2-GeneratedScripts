using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000179: Albert
/// </summary>
public class _11000179 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;70
    }

    // Select 0:
    // $script:0831180407000738$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000741$
                // - $MyPCName$, huh? You have a very... fitting name.
                return -1;
            case (70, 0):
                // $script:0831180407000742$
                // - Ah, we meet again. Thank you for taking care of things last time. I was able to score the contract thanks to you!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
