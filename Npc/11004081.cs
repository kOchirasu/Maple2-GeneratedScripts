using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004081: Strange Tombstone
/// </summary>
public class _11004081 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010249$
    // - <font color="#909090">(You faintly make out the cries of a woman. She somehow sounds far away and close at the same time.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010250$
                // - <font color="#909090">(You faintly make out the cries of a woman. She somehow sounds far away and close at the same time.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010251$
                // - My child... My child... Where are you...?
                return 10;
            case (10, 2):
                // $script:0619202207010252$
                // - Come back to me... Come out of the cold... Your mama is waiting...
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
