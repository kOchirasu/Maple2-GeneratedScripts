using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004263: The Sea Siren
/// </summary>
public class _11004263 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011182$
    // - <font color="#909090">(You see a large ship, which looks like it drifted here long, long ago.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011183$
                // - <font color="#909090">(You see a large ship, which looks like it drifted here long, long ago.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011184$
                // - <font color="#909090">(Its name is written on the side, faded by age and the elements. "The Sea Siren," it says. Then, in smaller text, "Fairy of the seas, protect our way.")</font>
                return 10;
            case (10, 2):
                // $script:0911203207011185$
                // - <font color="#909090">(Scattered chests litter the area, and you spy some items not native to Karkar. It must have been a merchant vessel.)</font>
                return 10;
            case (10, 3):
                // $script:0911203207011186$
                // - <font color="#909090">(Amidst the upheaval, you notice a large deformation on the side of the ship... and broken bones everywhere.)</font>
                return 10;
            case (10, 4):
                // $script:0911203207011187$
                // - <font color="#909090">(Could some terrible creature of the seas have caused all this mayhem and destruction?)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
