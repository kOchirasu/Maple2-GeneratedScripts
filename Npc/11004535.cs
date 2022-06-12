using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004535: Barricade Patrolman
/// </summary>
public class _11004535 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104170807012603$
    // - I'm sick of fighting! Is there no end to them?! <b>Oh...!</b> Hello, $male:Sir,female:Ma'am$! I didn't see you there!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104170807012604$
                // - I'm sick of fighting! Is there no end to them?! <b>Oh...!</b> Hello, $male:Sir,female:Ma'am$! I didn't see you there!
                return 10;
            case (10, 1):
                // $script:0104170807012605$
                // - This is the biggest road to and from $map:02020041$. Maybe that's why the enemy keeps hammering us here.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
