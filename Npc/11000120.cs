using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000120: 
/// </summary>
public class _11000120 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (10, NpcTalkButton.Close);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0831180407000519$ 
                // - Select a thread.
                return default;
            case 10:
                // $script:0831180407000520$ 
                // - This road is fraught with danger. You will need to make a detour.
                //   - Voice of experience
                return default;
        }
        
        return default;
    }
}
