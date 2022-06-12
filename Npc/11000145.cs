using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000145: Andy
/// </summary>
public class _11000145 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000611$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000613$
                // - Ugh... I feel dizzy... 
                switch (selection) {
                    // $script:0831180407000614$
                    // - Who are you?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000615$
                // - Name's $npcName:11000145[gender:0]$. You?
                switch (selection) {
                    // $script:0831180407000616$
                    // - I'm $MyPCName$.
                    case 0:
                        return 22;
                }
                return -1;
            case (22, 0):
                // $script:0831180407000617$
                // - $MyPCName$? That sounds familiar... Was that when I lost my pocket watch?
                switch (selection) {
                    // $script:0831180407000618$
                    // - Do you know me?
                    case 0:
                        return 23;
                }
                return -1;
            case (23, 0):
                // $script:0831180407000619$
                // - Oh, no. Your name just sounds familiar to me. I've been to so many places that sometimes I get names mixed up. Being here in the past is really... 
                return 23;
            case (23, 1):
                // $script:0831180407000620$
                // - Ahh, never mind. I'm talking nonsense now. Sigh... If you'll excuse me, I have things to do... 
                return -1;
            case (30, 0):
                // $script:0831180407000621$
                // - I'm sorry, but there's nothing more I can tell you about $npcName:22000322[gender:0]$ or the strange man wearing a $item:11300119$. Or, wait, have you asked yet?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.SelectableDistractor,
            (23, 0) => NpcTalkButton.Next,
            (23, 1) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
