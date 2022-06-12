using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001373: Sharmobi
/// </summary>
public class _11001373 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005348$
    // - Wah! You startled me!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005351$
                // - Sigh... I haven't been back home since I moved to Minar with my husband. I was so looking forward to this trip, and now the train has broken down...
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
