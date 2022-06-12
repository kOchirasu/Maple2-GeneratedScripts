using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000253: Mino
/// </summary>
public class _11000253 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0831180610000391$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0831180610000395$
                // - Prepare your hair for the <i>unimaginable</i>. The wild beast in my soul will <i>possess</i> these scissors and summon your desired hairstyle from your memories.
                switch (selection) {
                    // $script:0831180610000396$
                    // - Do it! I'm ready!
                    case 0:
                        return 0;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableBeauty,
            _ => NpcTalkButton.None,
        };
    }
}
