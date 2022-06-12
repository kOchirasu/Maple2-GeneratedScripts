using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11200005: Shuenji
/// </summary>
public class _11200005 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0518100907008515$
    // - The guild could use your help. You will be compensated!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0518100907008518$
                // - Complete this simple task, and you will get guild experience, funds, and some experience for yourself, too! Note that you can't start daily quests until you've been in the guild for a day, and you can't start weekly quests until you've been in the guild for a week.
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
