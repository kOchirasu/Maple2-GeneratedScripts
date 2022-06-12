using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004281: Unmarked Sarcophagus
/// </summary>
public class _11004281 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011294$
    // - <font color="#909090">(This sarcophagus has no name engraved upon it. Does an ancient lumarigon slumber within?)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011295$
                // - <font color="#909090">(This sarcophagus has no name engraved upon it. Does an ancient lumarigon slumber within?)</font>
                return 10;
            case (10, 1):
                // $script:0913151207011307$
                // - <font color="#909090">(It's covered in a thick layer of dust. Still, the elaborate carvings are the work of a master artisan.)</font>
                return 10;
            case (10, 2):
                // $script:0913151207011308$
                // - <font color="#909090">(As you gaze upon the sarcophagus, you're overcome by a sudden feeling of melancholy.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
