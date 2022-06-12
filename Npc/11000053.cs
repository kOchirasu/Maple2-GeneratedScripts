using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000053: Luen
/// </summary>
public class _11000053 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000227$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000230$
                // - $MyPCName$! Are you here to make some money? The court festival must be great for business. Everywhere I look, folks are out doing something for it.
                return -1;
            case (40, 0):
                // $script:0831180407000231$
                // - The priciest thing to come out of all this is $itemPlural:20000013$, and you can only get them from Turtle Hill, where $npcName:22300149$ is.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
