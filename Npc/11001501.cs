using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001501: Dunba
/// </summary>
public class _11001501 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0118150907005840$
    // - You know I outrank you, right? Hah hah!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005843$
                // - Don't just stare at your food, eat it! So rude.
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
