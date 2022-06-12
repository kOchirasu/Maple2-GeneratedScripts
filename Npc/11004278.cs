using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004278: Shadow Dragon Statue
/// </summary>
public class _11004278 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011283$
    // - <font color="#909090">(You feel an ominous chill as you gaze upon the dragon statue.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011284$
                // - <font color="#909090">(You feel an ominous chill as you gaze upon the dragon statue.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011285$
                // - <font color="#909090">(This statue was once a grand piece of architecture, proudly displaying the spirit of the dragons. However, it's been altered by darkness.)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011286$
                // - <font color="#909090">(The power of the dragons of light which once protected Nazkar is completely gone. Now, all avoid this once-sacred area.)</font>
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
