using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000065: Marco
/// </summary>
public class _11000065 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000336$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000338$
                // - As the mayor, I have a serious dilemma. Should I make the city great again, or is it already great?
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
