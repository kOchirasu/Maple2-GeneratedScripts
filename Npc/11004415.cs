using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004415: Frosty Fairfolk
/// </summary>
public class _11004415 : NpcScript {
    internal _11004415(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1120173007011889$ 
                // - The fairfolk's cake is so, so sweet!
                return true;
            case 10:
                // $script:1120173007011892$ 
                // - The fairfolk's cake is so, so sweet!
                // $script:1120173007011894$ 
                // - Eat all you want, and it never never runs out! It's <i>magic cake</i>. That's the best part! Hee hee!
                return true;
            default:
                return true;
        }
    }
}
