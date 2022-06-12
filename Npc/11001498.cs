using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001498: Dunba
/// </summary>
public class _11001498 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0118150907005828$
    // - You know I outrank you, right? Hah hah!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005831$
                // - Don't just stare at your food, eat it! So rude.
                switch (selection) {
                    // $script:0120170607005853$
                    // - Tell me about your past.
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0120170607005854$
                // - If not for him...
                return -1;
            case (32, 0):
                // $script:0120170607005855$
                // - I'm sorry, but I just want to eat right now.
                return -1;
            case (40, 0):
                // $script:0127102807005857$
                // - Don't just stare at your food, eat it! So rude.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
