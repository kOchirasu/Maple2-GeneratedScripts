using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004262: Small Pond
/// </summary>
public class _11004262 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011177$
    // - <font color="#909090">(This pleasant little pond holds a prominent position in $npcName:11001350[gender:0]$'s estate.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011178$
                // - <font color="#909090">(This pleasant little pond holds a prominent position in $npcName:11001350[gender:0]$'s estate.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011179$
                // - <font color="#909090">(The fish look like golden bladefish, a species unique to the island.)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011180$
                // - <font color="#909090">(Their scales shimmer beautifully in the sunlight. The interplay of light brings a sense of peace to your mind...)</font>
                return 10;
            case (10, 3):
                // $script:0911203207011181$
                // - <font color="#909090">(Maybe it's time you got some fish of your own.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
