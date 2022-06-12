using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004536: Barricade Patrolman
/// </summary>
public class _11004536 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104170807012607$
    // - Don't worry. I've got my eye on the enemy movements.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104170807012608$
                // - Don't worry. I've got my eye on the enemy movements.
                return 10;
            case (10, 1):
                // $script:0104170807012609$
                // - There are no signs of an enemy attack, but that can change in an instant. That's why we can't slack off on our patrols!
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
