using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000118: Cliffine
/// </summary>
public class _11000118 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000503$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000506$
                // - Usually this place is not so crowded. I didn't expect so many people to be so eager to make money. 
                return 30;
            case (30, 1):
                // $script:0831180407000507$
                // - $MyPCName$, you looking to scare up some cash too? It's not as dangerous as I expected. Give it a try!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
