using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000379: Seymour Vistas
/// </summary>
public class _11000379 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001550$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001552$
                // - Heya! I'm $npcName:11000379[gender:0]$, and I'm a member of the Wall Climbers. We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
