using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001311: Ronan
/// </summary>
public class _11001311 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1215203907005030$
    // - Glory to the empress!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1227194507005664$
                // - I've never been this far from home before. I miss my family...
                return 30;
            case (30, 1):
                // $script:1227194507005665$
                // - My friends envied me for getting to go on this trip. I was excited, too. But the day before I left, I was already feeling homesick.
                return 30;
            case (30, 2):
                // $script:1227194507005666$
                // - You're amazing, you know that? You've been far from home even longer than I have, and it doesn't show. I've got to work to be as strong as you someday!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
