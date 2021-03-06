using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001009: Fachinni
/// </summary>
public class _11001009 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003442$
    // - Wah! Geez!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003445$
                // - Are you also here because of that beanstalk rumor?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
