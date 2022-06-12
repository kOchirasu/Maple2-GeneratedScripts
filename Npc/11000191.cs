using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000191: Mrs. Hofmann
/// </summary>
public class _11000191 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000858$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000861$
                // - I think my husband should've married his job instead of me. He's never home.
                return -1;
            case (30, 0):
                // $script:0831180407000862$
                // - I used to love the aroma of herbs that followed my husband, but that was before we married. He's so obsessed with them now that he never has time to help around the house.
                return 30;
            case (30, 1):
                // $script:0831180407000863$
                // - Sometimes I wonder... I wonder if I should take the kids to $map:02000002$ for a fresh start. There's more to being a good husband than just putting food on the table. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
