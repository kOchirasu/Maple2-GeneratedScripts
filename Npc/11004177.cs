using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004177: Eve
/// </summary>
public class _11004177 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010616$
    // - Yes? How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010617$
                // - You want to join our squad? Listen, you seem nice, but I've already got two reliable partners. I don't think we need anyone else.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
