using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001072: Brave Tree Spirit
/// </summary>
public class _11001072 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003655$
    // - Go away.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003658$
                // - You're from the outside world, aren't you? What are you going to change here this time?
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
