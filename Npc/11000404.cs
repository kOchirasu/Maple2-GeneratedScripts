using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000404: Snowy
/// </summary>
public class _11000404 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;60
    }

    // Select 0:
    // $script:0831180407001634$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001638$
                // - $npcName:23000024[gender:1]$ carries a dark power. Try not to get poisoned.
                return -1;
            case (60, 0):
                // $script:0831180407001639$
                // - Some folks think I must be a blacksmith. But not all yetis are smiths, you know! So stop trying to buy my stuff.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
