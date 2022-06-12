using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000126: Poffo
/// </summary>
public class _11000126 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000545$
    // - Um... Hi. What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000548$
                // - I mustered up the courage to come here, but now I'm too scared to move. I have to hunt monsters, or get the treasure from the cliff. I need the money...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
